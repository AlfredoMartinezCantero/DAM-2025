public class Playlist {

    // 1. Declaración de variables (Atributos de la clase)
    String nombrePlaylist;
    int numeroCanciones;
    String[] listaCanciones;

    // Constructor para inicializar las variables
    public Playlist() {
        // 2. Inicialización de variables
        this.nombrePlaylist = "Extremoduro - Grandes Éxitos";
        this.numeroCanciones = 5;
        
        // Inicializo el array con 5 canciones concretas
        this.listaCanciones = new String[] {
            "So Payaso", 
            "La Vereda de la Puerta de Atrás", 
            "Standby", 
            "Golfa", 
            "Jesucristo García"
        };
    }

    // 3. Método para agregar canciones
    public void agregarCancion(String cancion) {
        // Como el array es estático, creo uno nuevo con un hueco más (+1)
        String[] nuevaLista = new String[this.numeroCanciones + 1];

        // Copio las canciones que ya tenía
        for (int i = 0; i < this.numeroCanciones; i++) {
            nuevaLista[i] = this.listaCanciones[i];
        }

        // Añado la nueva canción en la última posición
        nuevaLista[this.numeroCanciones] = cancion;

        // Actualizo mis variables para que apunten a la nueva lista
        this.listaCanciones = nuevaLista;
        this.numeroCanciones++; // Aumento el contador
        
        System.out.println(">> Canción añadida: " + cancion);
    }

    // 4. Método para reproducir todas las canciones
    public void reproducirPlaylist() {
        System.out.println("\n--- Reproduciendo: " + this.nombrePlaylist + " ---");
        for (int i = 0; i < this.numeroCanciones; i++) {
            // Sumo 1 a 'i' solo para que visualmente quede "1. Cancion", "2. Cancion"...
            System.out.println((i + 1) + ". " + this.listaCanciones[i]);
        }
        System.out.println("----------------------------------------\n");
    }

    // 5. Método para eliminar una canción
    public void eliminarCancion(String cancion) {
        // Primero busco si la canción existe y en qué posición está
        int indiceEncontrado = -1;
        
        for (int i = 0; i < this.numeroCanciones; i++) {
            // OJO: En Java los String se comparan con .equals(), no con ==
            if (this.listaCanciones[i].equals(cancion)) {
                indiceEncontrado = i;
                break; // Ya la encontré, dejo de buscar
            }
        }

        if (indiceEncontrado != -1) {
            // Si existe, creo un array con un hueco menos (-1)
            String[] nuevaLista = new String[this.numeroCanciones - 1];
            
            int j = 0; // Índice para la nueva lista
            for (int i = 0; i < this.numeroCanciones; i++) {
                // Si NO es la canción que quiero borrar, la copio
                if (i != indiceEncontrado) {
                    nuevaLista[j] = this.listaCanciones[i];
                    j++;
                }
            }
            
            // Actualizo las referencias
            this.listaCanciones = nuevaLista;
            this.numeroCanciones--;
            System.out.println(">> Canción eliminada: " + cancion);
        } else {
            System.out.println(">> Error: La canción '" + cancion + "' no está en la lista.");
        }
    }

    // Método Main para probar que todo funciona (Test)
    public static void main(String[] args) {
        Playlist miMusica = new Playlist();

        miMusica.reproducirPlaylist(); // Muestra las 5 iniciales

        miMusica.agregarCancion("Salir"); // Añado la 6ª
        miMusica.reproducirPlaylist();

        miMusica.eliminarCancion("Standby"); // Borro una del medio
        miMusica.reproducirPlaylist();
    }
}