let amountReceived = 0;
let numberSold = 0;

function finishSale() {
    if (++numberSold >= 3)
        $('#continue-market').removeClass('hidden disabled');
    $('#amount-received').text(amountReceived.toFixed(2));
}

$(function () {
    $('#farm-equip-sold').on('navi', function () {
        amountReceived += 19.22;
        $('#enter-farm-equip-sell').addClass('disabled');
        finishSale();
    });
    $('#wagon-sold').on('navi', function () {
        amountReceived += 12.40;
        $('#enter-wagon-sell').addClass('disabled');
        finishSale();
    });
    $('#placeholder-sold').on('navi', function () {
        amountReceived += 6.34;
        $('#enter-placeholder-sell').addClass('disabled');
        finishSale();
    });
});
