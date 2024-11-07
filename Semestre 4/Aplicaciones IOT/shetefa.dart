import 'dart:io';

class Item {
  String name;
  bool isPurchased;

  Item(this.name, {this.isPurchased = false});
}

void main() {
  List<Item> shoppingList = [];

  while (true) {
    print('\nLista de Compras:');
    print('1. Agregar articulo');
    print('2. Eliminar articulo');
    print('3. Mostrar articulos');
    print('4. Marcar articulo como comprado');
    print('5. Salir');
    stdout.write('Selecciona una opcion: ');
    String? choice = stdin.readLineSync();

    switch (choice) {
      case '1':
        stdout.write('Nombre del articulo: ');
        String? name = stdin.readLineSync();
        if (name != null && name.isNotEmpty) {
          shoppingList.add(Item(name));
          print('Articulo agregado.');
        } else {
          print('Nombre no valido.');
        }
        break;
      case '2':
        stdout.write('Nombre del articulo para eliminar: ');
        String? name = stdin.readLineSync();
        shoppingList.removeWhere((item) => item.name == name);
        print('Articulo eliminado.');
        break;
      case '3':
        print('\nArticulos en la lista:');
        for (var item in shoppingList) {
          print('${item.name} ${item.isPurchased ? "(Comprado)" : ""}');
        }
        break;
      case '4':
        stdout.write('Nombre del articulo comprado: ');
        String? name = stdin.readLineSync();
        for (var item in shoppingList) {
          if (item.name == name) {
            item.isPurchased = true;
            print('Articulo marcado como comprado.');
            break;
          }
        }
        break;
      case '5':
        print('Saliendo...');
        return;
      default:
        print('Opcion no valida.');
    }
  }
}
