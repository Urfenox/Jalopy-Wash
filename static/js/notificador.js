window.onload = () => {
    function askNotificationPermission() {
        // Function to actually ask the permissions
        function handlePermission(permission) {
            // Whatever the user answers, we make sure Chrome stores the information
            if (!Reflect.has(Notification, 'permission')) {
                Notification.permission = permission;
            }
        };
  
        // Check if the browser supports notifications
        if (!Reflect.has(window, 'Notification')) {
            console.log('This browser does not support notifications.');
        } else {
            if (checkNotificationPromise()) {
                Notification.requestPermission().then(handlePermission);
            } else {
                Notification.requestPermission(handlePermission);
            }
        }
    };
    function checkNotificationPromise() {
        try {
            Notification.requestPermission().then();
        } catch(e) {
            return false;
        }
        return true;
    };
    if (Notification.permission === 'granted') {
        function checkNotify() {
            const url = window.location.href;
            fetch(
                url,
                {
                    method: "GET",
                    headers: {
                        'Content-Type': 'application/json'
                    }
                }
            )
            .then((respuesta => respuesta.json()))
            .then((respuesta) => {
                console.log(respuesta);
                if (respuesta.estado == "PENDIENTE") {
                    let title = "Aviso de hora";
                    const img = 'https://github.com/mdn/dom-examples/blob/main/to-do-notifications/img/icon-128.png';
                    const text = `¡Hola, ${respuesta.dueño}! Ya puedes traernos tu coche ${respuesta.patente}.`;
                    const notification = new Notification(title, { body: text, icon: img });
                    clearInterval(notificador);
                }
            });
        }
        const notificador = setInterval(checkNotify, 5000);
    }
    askNotificationPermission();
};