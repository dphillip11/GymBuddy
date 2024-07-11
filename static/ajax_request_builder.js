class AjaxRequestBuilder {
    constructor(selector) {
        this.selector = selector;
        this.event = null;
        this.method = 'GET';
        this.route = '';
        this.params = {};
        this.successCallback = null;
        this.errorCallback = null;
        this.headers = {};
    }

    onEvent(event) {
        this.event = event;
        return this;
    }

    withPost(route) {
        this.method = 'POST';
        this.route = route;
        return this;
    }

    withGet(route) {
        this.method = 'GET';
        this.route = route;
        return this;
    }

    withParams(params) {
        this.params = params;
        return this;
    }

    withHeaders(headers) {
        this.headers = headers;
        return this;
    }

    onSuccess(callback) {
        this.successCallback = callback;
        return this;
    }

    onError(callback) {
        this.errorCallback = callback;
        return this;
    }

    build() {
        document.querySelector(this.selector).addEventListener(this.event, (event) => {
            event.preventDefault(); // Prevent default action for form submissions

            fetch(this.route, {
                method: this.method,
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'X-CSRFToken': this.getCsrfToken(),
                    ...this.headers  // Merge custom headers
                },
                body: this.method === 'POST' ? new URLSearchParams(this.params) : null
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                if (this.successCallback) {
                    this.successCallback(data);
                }
            })
            .catch(error => {
                if (this.errorCallback) {
                    this.errorCallback(error);
                } else {
                    console.error('Fetch error:', error);
                }
            });
        });
    }

    // Helper method to get the CSRF token from the meta tag
    getCsrfToken() {
        return document.querySelector('meta[name="csrf-token"]').getAttribute('content');
    }

    // Handle form submissions with FormData
    handleFormSubmission(formSelector) {
        this.selector = formSelector;
        this.event = 'submit';
        this.method = 'POST';
        return this;
    }
}