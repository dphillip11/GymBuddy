// respond to websocket
document.addEventListener("DOMContentLoaded", function() {
        // Retrieve the WebSocket URL from a global variable or meta tag
        const socket = new WebSocket('ws://' + window.location.host + '/update_items/');

        socket.onopen = function(event) {
            console.log('WebSocket connection established:', event);
        };

        socket.onmessage = function(event) {

            const data = JSON.parse(event.data);
            const elementId = data.element_id;
            const htmlContent = data.new_content;
            const append = data.append;

            // Create a new element from the HTML content
            const newElement = document.createElement('div');
            newElement.innerHTML = htmlContent;

            const forms = newElement.querySelectorAll('form');
            forms.forEach(form => {
                let csrfInput = form.querySelector('input[name="csrfmiddlewaretoken"]');
                if (csrfInput) {
                    csrfInput.value = window.csrfToken;
                    console.log("CSRF token updated in form");
                } else {
                    // If there's no csrfmiddlewaretoken input, create one
                    const newCsrfInput = document.createElement('input');
                    newCsrfInput.type = 'hidden';
                    newCsrfInput.name = 'csrfmiddlewaretoken';
                    newCsrfInput.value = window.csrfToken;
                    form.appendChild(newCsrfInput);
                    console.log("CSRF token added to form");
                }
            });

            const newContent = newElement.firstChild;

            // Find the element with the given ID and update its innerHTML
            const targetElement = document.querySelector(`#${elementId}`);
            if (targetElement) {
                if (append )
                    targetElement.insertAdjacentHTML('beforeend', htmlContent);
                else
                {
                    targetElement.replaceWith(newContent);
                }

                console.log(`Updated ${elementId} with new content.`);
            } else {
                console.warn(`Element with ID ${elementId} not found.`);
            }
        };

        socket.onerror = function(error) {
            console.error('WebSocket Error:', error);
        };

        socket.onclose = function(event) {
            console.log('WebSocket connection closed:', event);
        };
    });