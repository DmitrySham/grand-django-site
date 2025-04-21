var timeoutRef = { current: null };

$(document).ready(function () {
  const actionField = $('#id_action');

  if (actionField.length > 0) {
    const paymentUrlField = $('.field-payment_url');

    actionField.each(function () {
      let $this = $(this);

      const toggleField = () => {
        if ($this.val() === 'redirect') {
          paymentUrlField.fadeIn();
        } else {
          paymentUrlField.fadeOut();
        }
        timeoutRef.current = null;
      }

      this.onchange = () => {
        if (timeoutRef.current) {
          clearTimeout(timeoutRef.current);
          timeoutRef.current = null;
        }

        timeoutRef.current = setTimeout(toggleField, 100);
      };
      toggleField();
    })
  }
});
