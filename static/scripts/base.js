let selectedIndex;
let selected;

let pageIndex;
let page;

function up() {
    if (selectedIndex > 0)
        changeSelected(selectedIndex - 1);
}

function down() {
    if (selectedIndex < page.find('.opt').length - 1)
        changeSelected(selectedIndex + 1);
}

function changeSelected(newIndex) {
    let old = selected;
    selected = $(page.find('.opt')[newIndex]);
    if (selected.hasClass('hidden')) {
        selected = old;
        return;
    }

    old.removeClass('selected');
    old.blur();

    selectedIndex = newIndex;
    selected.addClass('selected');
    selected.focus();
}

function enter() {
    if (selected.hasClass('disabled'))
        return;
    if (selected.hasClass('submit'))
        selected.parent().submit();
    else if (selected.hasClass('navi')) {
        if (selected.hasClass('navi-next'))
            changePage(pageIndex + 1);
        else if (selected.hasClass('navi-prev'))
            changePage(pageIndex - 1);
        else if (selected.hasClass('navi-page')) {
            let page = $(`#${selected.attr('data-navi')}`);
            // get index of the page
            const index = $('.page').index(page);
            changePage(index);
        }
        selected.trigger('navi');
    }
}

function changePage(newPage) {
    const pages = $('.page');
    page.addClass('d-none');
    pageIndex = newPage;
    page = $(pages[pageIndex]);
    page.removeClass('d-none');
    changeSelected(0);
}

$(function () {
    page = $($('.page')[0]);
    pageIndex = 0;
    selectedIndex = 0;
    selected = $(page.find('.opt')[0]);

    changePage(0);
    changeSelected(0);

    $(document).on("keydown", function (e) {
        switch (e.which) {
            case 38:
                up();
                e.preventDefault();
                break;
            case 40:
                down();
                e.preventDefault();
                break;
            case 13:
                enter();
                e.preventDefault();
                break;
            case 9: // tab
                e.preventDefault();
                break;
        }
    });

    $(document).on("click mouseup mousedown dblclick", function (e) {
        e.preventDefault();
    });
});
