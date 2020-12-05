function FormViewer(props) {
    props = props || {};
    props.fieldSelector = props.fieldSelector || '#id_form_data';
    props.postField = props.postField || '.field-get_post_display';

    this.regex = /\[[#](\d+?)\]/gi;
    this.field = $(props.fieldSelector);
    this.postField = $($(props.postField).find('p'));

    this.init = () => {
        this.renderForm();
        this.renderPost();
    };

    this.getFormTemplate = values => {
        if (!Object.keys(values).length) return [
            '<div class="form-viewer">',
                'Данных нет',
            '</div>'
        ].join('');

        return [
            '<div class="form-viewer">',
                Object
                    .keys(values)
                    .map(key => `<div class="field-item"><b>${key}</b>: ${values[key]}</div>`)
                    .join('\n'),
            '</div>'
        ].join('\n')
    };

    this.getInitialValue = () => {
        try {
            return JSON.parse(this.field.val());
        } catch (e) {
            console.error(e);
            return {};
        }
    };

    this.renderForm = () => {
        this.field.css('display', 'none');

        const template = this.getFormTemplate(this.getInitialValue());

        this.field
            .parent()
            .append(template);
    };

    this.getPostTemplate = ({ id, title, slug }) => [
        title && `<b>${title}</b>`,
        ' | ',
        id && `<a class="post-link" target="_blank" href="/admin/blog/post/${id}/change/">Посмотреть в админке</a>`,
        ' | ',
        slug && `<a class="post-link" target="_blank" href="/news/posts/${slug}/">Посмотреть на сайте</a>`
    ].filter(Boolean).join('\n');

    this.getPostData = () => {
        try {
            return JSON.parse(this.postField.text());
        } catch (e) {
            return {};
        }
    };

    this.renderPost = () => {
        const postData = this.getPostData();

        if (postData && postData.id) {
            const template = this.getPostTemplate(postData);
            this.postField.html(template);
        }
    };

    return this;
}

$(document).ready(() => {
    window.formViewer = new FormViewer();
    formViewer.init();
});
