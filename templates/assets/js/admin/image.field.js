function ImageField(options) {
    options = options || {};
    options.selector = options.selector || 'input[type="file"]';
    options.initialPreviewerClass = options.initialPreviewerClass || 'image-field-initial-previewer';
    options.previewerClass = options.previewerClass || 'image-field-previewer';

    this.instances = [];

    this.init = () => {
        if (typeof $.fn.hasAttr !== 'function') {
            $.fn.hasAttr = function(value) {
                return this.attr(value) !== undefined && this.attr(value) !== null;
            }
        }

        this.elements = $(options.selector);
        this.elements.each(this.initField);
    };

    this.initField = (idx, item) => {
        const instance = {
            item: $(item),
            idx: idx,
            initialValue: this.getInitialValue(item),
            previewer: this.renderPreviewWrapper(item, idx),
            name: $(item).attr('id').replace('id_', ''),
        };

        if (instance.initialValue) {
            instance.initialPreviewer = this.renderInitialPreviewWrapper(item, idx);

            instance.initialPreviewer.html(this.getImageTemplate({
                idx,
                url: instance.initialValue
            }));
            this.initFancyBox();
        }

        instance.item.off('change');
        instance.item.on('change', e => {
            if (!e.target.files.length) return;

            this.renderImage(e.target.files[0], instance);
        });

        this.instances.push(instance);
    };

    this.getInitialValue = (item) => {
        const parent = $(item).parent();

        if (
            !parent.length
            || parent[0].tagName.toLowerCase() !== 'p'
            || !parent.find('a').length
        ) return null;

        const linkEl = parent.find('a').first();

        return linkEl.attr('href');
    };

    this.getImageTemplate = ({ url, idx }) => [
        `<div class="image-item" data-index="${idx}">`,
            `<a href="${url}" data-fancybox="gallery"><img src="${url}" alt="Uploaded image" /></a>`,
        '</div>',
    ].filter(Boolean).join('\n');

    this.renderInitialPreviewWrapper = (el, idx) => {
        $(el).parent().prepend(`<div class="${options.initialPreviewerClass}" data-idx="${idx}"></div>`);
        return $(`.${options.initialPreviewerClass}[data-idx="${idx}"]`).first();
    };

    this.renderPreviewWrapper = (el, idx) => {
        $(el).parent().append(`<div class="${options.previewerClass}" data-idx="${idx}"></div>`);
        return $(`.${options.previewerClass}[data-idx="${idx}"]`).first();
    };

    this.renderImage = (file, instance) => {
        const fileReader = new FileReader();
        fileReader.readAsDataURL(file);
        fileReader.onloadend = ({ target }) => {
            instance.previewer.html(this.getImageTemplate({
                idx: instance.idx,
                url: target.result,
            }));
            this.initFancyBox();
        };
    };

    this.initFancyBox = () => {
        $('[data-fancybox="gallery"]').fancybox();
    };

    return this;
}


$(document).ready(() => {
    window.imageFields = new ImageField();
    imageFields.init();
});