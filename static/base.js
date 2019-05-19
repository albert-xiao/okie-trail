let selectedIndex;
let selected;

function up() {
    if (selectedIndex > 0)
        changeSelected(selectedIndex - 1);
}

function down() {
    if (selectedIndex < $('.opt').length - 1)
        changeSelected(selectedIndex + 1);
}

function changeSelected(newIndex) {
    selectedIndex = newIndex;
    selected.removeClass('selected');
    selected.blur();

    selected = $($('.opt')[selectedIndex]);
    selected.addClass('selected');
    selected.focus();
}

function enter() {
    if (selected.hasClass('submit'))
        selected.parent().submit();
}

$(function () {
    selectedIndex = 0;
    selected = $($('.opt')[0]);
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
            case 9:
                e.preventDefault();
                break;
        }
    });

    $(document).on("click mouseup mousedown dblclick", function (e) {
        e.preventDefault();
    });
});
