function CheckoutRequest(options) {
    this.options = options || {};
    this.url = options.url || null;
    this.modelName = options.modelName || null;
    this.modelId = options.modelId || null;
    this.form = options.form || '#checkoutForm';
    this.modal = options.modal || '#checkoutModal';

    this.data = {
        csrfmiddlewaretoken: getCookie('csrftoken'),
        is_agree: this.form.find('#is_agree')[0].is(":checked"),
        name: this.form.find('#id_name').val(),
        email: this.form.find('#id_email').val(),
        message: this.form.find('#id_message').val(),
        model_id: this.modelId,
        model_name: this.modelName
    };

    this.init = () => {
        this.formSubmit()

    };
    this.formSubmit = () => {
        this.getForm.on('submit', (e) => {
            e.preventDefault();
            this.ajaxRequest()
        })
    };

    this.ajaxRequest = () => {
        console.log('ajaxRequest');
        $.ajax({
            url: this.url,
            method: 'POST',
            dataType: 'JSON',
            data: this.data,

            success: (response) => {
                this.geModal.modal("hide");
                alert(response.message)
            },
            error: (request, errThrown, errObject) => {
                this.geModal.modal("hide");
                console.error(request, errThrown, errObject);
            }
        })
    };

    this.geModal = () => {
        return $(this.modal);
    };

    this.getForm = () => {
        return $(this.form)
    };

    return this;
}