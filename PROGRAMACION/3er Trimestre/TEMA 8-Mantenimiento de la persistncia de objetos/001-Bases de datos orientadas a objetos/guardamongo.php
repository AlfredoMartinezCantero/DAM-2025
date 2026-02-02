<?php
// guardamongo.php
// Requires: sudo apt install php-mongodb
declare(strict_types=1);

header('Content-Type: application/json; charset=utf-8');

// --- Helpers ---
function respond(int $code, array $payload): void {
  http_response_code($code);
  echo json_encode($payload, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES);
  exit;
}

function clean_price_to_float($price): float {
  // Accept "12€", "12.50€", "12,50€", 12, "12.5", etc.
  if (is_numeric($price)) return (float)$price;

  $s = (string)$price;
  $s = trim($s);
  $s = str_replace(['€', 'EUR', ' '], '', $s);
  $s = str_replace(',', '.', $s); // comma decimals -> dot
  // keep digits and dot only
  $s = preg_replace('/[^0-9.]/', '', $s) ?? '';
  if ($s === '' || !is_numeric($s)) return 0.0;
  return (float)$s;
}

// --- Get JSON input (GET ?json=... OR POST raw JSON) ---
$json = null;

if (isset($_GET['json'])) {
  $json = $_GET['json'];
} else {
  $raw = file_get_contents('php://input');
  if ($raw !== false && trim($raw) !== '') {
    $json = $raw;
  }
}

if ($json === null || trim($json) === '') {
  respond(400, [
    'ok' => false,
    'error' => 'missing_json',
    'message' => 'No JSON received. Send ?json=... or POST a JSON body.'
  ]);
}

// URL-decoding for GET parameter (important if fetch encodes it)
$json = urldecode($json);

$data = json_decode($json, true);
if (!is_array($data)) {
  respond(400, [
    'ok' => false,
    'error' => 'invalid_json',
    'message' => 'JSON could not be decoded.'
  ]);
}

// --- Minimal validation based on your front structure ---
if (!isset($data['cliente']) || !is_array($data['cliente'])) {
  respond(400, ['ok' => false, 'error' => 'invalid_payload', 'message' => 'Missing cliente object.']);
}
if (!isset($data['productos']) || !is_array($data['productos'])) {
  respond(400, ['ok' => false, 'error' => 'invalid_payload', 'message' => 'Missing productos array.']);
}
if (!isset($data['pedido']) || !is_array($data['pedido'])) {
  respond(400, ['ok' => false, 'error' => 'invalid_payload', 'message' => 'Missing pedido object.']);
}

// Basic required fields
$nombre    = trim((string)($data['cliente']['nombre'] ?? ''));
$apellidos = trim((string)($data['cliente']['apellidos'] ?? ''));
$email     = trim((string)($data['cliente']['email'] ?? ''));
$numero    = $data['pedido']['numero'] ?? null;
$fecha     = trim((string)($data['pedido']['fecha'] ?? ''));

if ($nombre === '' || $apellidos === '' || $email === '' || !filter_var($email, FILTER_VALIDATE_EMAIL)) {
  respond(400, [
    'ok' => false,
    'error' => 'invalid_customer',
    'message' => 'Customer data missing or email invalid.'
  ]);
}
if ($numero === null || $fecha === '') {
  respond(400, [
    'ok' => false,
    'error' => 'invalid_order',
    'message' => 'Order numero/fecha missing.'
  ]);
}

// --- Normalize products + totals ---
$items = [];
$total = 0.0;

foreach ($data['productos'] as $p) {
  if (!is_array($p)) continue;
  $pn = trim((string)($p['nombre'] ?? ''));
  $pp = $p['precio'] ?? 0;

  if ($pn === '') continue;

  $price = clean_price_to_float($pp);
  $items[] = [
    'nombre' => $pn,
    'precio' => $price
  ];
  $total += $price;
}

if (count($items) === 0) {
  respond(400, [
    'ok' => false,
    'error' => 'empty_cart',
    'message' => 'No products in order.'
  ]);
}

// --- Build document to insert ---
$doc = [
  'cliente' => [
    'nombre' => $nombre,
    'apellidos' => $apellidos,
    'email' => $email
  ],
  'productos' => $items,
  'pedido' => [
    'numero' => (string)$numero, // stored as string to avoid JS integer issues
    'fecha' => $fecha,
    'total' => $total,
    'currency' => 'EUR',
    'status' => 'new'
  ],
  '_created_at' => new MongoDB\BSON\UTCDateTime((int)(microtime(true) * 1000)),
  '_ip' => $_SERVER['REMOTE_ADDR'] ?? null,
  '_ua' => $_SERVER['HTTP_USER_AGENT'] ?? null
];

// --- Insert into MongoDB ---
try {
  $manager = new MongoDB\Driver\Manager('mongodb://127.0.0.1:27017');

  $bulk = new MongoDB\Driver\BulkWrite();
  $id = $bulk->insert($doc);

  $result = $manager->executeBulkWrite('microtienda.pedidos', $bulk);

  respond(200, [
    'ok' => true,
    'id' => (string)$id,
    'inserted' => $result->getInsertedCount(),
    'total' => $total
  ]);

} catch (Throwable $e) {
  respond(500, [
    'ok' => false,
    'error' => 'mongo_error',
    'message' => $e->getMessage()
  ]);
}
