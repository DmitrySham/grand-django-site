function PriceBox(options) {
    options = options || {};
    options.wrapper = options.wrapper || '#price-box';
    options.priceWrapper = options.priceWrapper || '#price-tag';

    this.wrapper = $(options.wrapper);
    this.items = this.wrapper.find('li');

    this.priceWrapper = $(options.priceWrapper);

    this.init = () => {
        this.items.each((i, obj) => {
            $(obj).on('click', e => {
                e.preventDefault();

                let $this = $(obj);

                if (!$this.hasClass('active')) {
                    let id = parseInt($this.attr('data-id'), 10);

                    this.setActive(id);
                }
            });
        });
    };

    this.setActive = id => {
        $(this.wrapper.find('li.active')).removeClass('active');

        const current = $(this.wrapper.find('li[data-id="' + id + '"]'));

        current.addClass('active');

        let price = current.attr('data-value');
        this.priceWrapper.html(price);
    };

    return this;
}