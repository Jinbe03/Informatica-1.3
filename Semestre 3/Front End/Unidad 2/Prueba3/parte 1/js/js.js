document.addEventListener('DOMContentLoaded', () => {
    const clienteForm = document.getElementById('clienteForm');
    const clientesList = document.getElementById('clientesList');
    const listadoClientesContainer = document.getElementById('listadoClientesContainer');

    clienteForm.addEventListener('submit', (e) => {
        e.preventDefault();

        const rut = document.getElementById('rut').value.trim();
        const nombre = document.getElementById('nombre').value.trim();
        const apellido = document.getElementById('apellido').value.trim();
        const edad = document.getElementById('edad').value.trim();
        const correo = document.getElementById('correo').value.trim();

        if (rut === '' || nombre === '' || apellido === '' || edad === '' || correo === '') {
            alert('Por favor, completa todos los campos.');
            return;
        }

        const correoRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!correoRegex.test(correo)) {
            alert('Por favor, ingresa un correo electrónico válido.');
            return;
        }

        const edadNum = parseInt(edad);
        if (isNaN(edadNum) || edadNum <= 0) {
            alert('Por favor, ingresa una edad válida.');
            return;
        }

        const cliente = { rut, nombre, apellido, edad : edadNum, correo };
        let clientes = JSON.parse(localStorage.getItem('clientes')) || [];

        const index = clientes.findIndex(c => c.rut === rut);
        if (index === -1) {
            clientes.push(cliente);
        } else {
            clientes[index] = cliente;
        }

        localStorage.setItem('clientes', JSON.stringify(clientes));
        clienteForm.reset();
        mostrarClientes();
    });

    function mostrarClientes() {
        clientesList.innerHTML = '';
        let clientes = JSON.parse(localStorage.getItem('clientes')) || [];

        clientes.forEach(cliente => {
            const li = document.createElement('li');
            li.innerHTML = `
                ${cliente.nombre} ${cliente.apellido} - ${cliente.edad} años - ${cliente.correo}
                <button onclick="eliminarCliente('${cliente.rut}')">Eliminar</button>
                <button onclick="modificarCliente('${cliente.rut}')">Modificar</button>
            `;
            clientesList.appendChild(li);
        });

        listadoClientesContainer.style.display = 'block';
    }

    window.eliminarCliente = function eliminarCliente(rut) {
        let clientes = JSON.parse(localStorage.getItem('clientes')) || [];
        clientes = clientes.filter(cliente => cliente.rut !== rut);
        localStorage.setItem('clientes', JSON.stringify(clientes));
        mostrarClientes();
    };

    window.modificarCliente = function modificarCliente(rut) {
        let clientes = JSON.parse(localStorage.getItem('clientes')) || [];
        const cliente = clientes.find(cliente => cliente.rut === rut);
        if (cliente) {
            document.getElementById('rut').value = cliente.rut;
            document.getElementById('nombre').value = cliente.nombre;
            document.getElementById('apellido').value = cliente.apellido;
            document.getElementById('edad').value = cliente.edad;
            document.getElementById('correo').value = cliente.correo;
        }
    };

    const storedClientes = JSON.parse(localStorage.getItem('clientes'));
    if (storedClientes && storedClientes.length > 0) {
        mostrarClientes();
    }
});

