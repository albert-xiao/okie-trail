$(function() {
    $('.trail.animate').on('oanimationend animationend webkitAnimationEnd', function() {
        $('.traveling').toggleClass('hidden');
        changeSelected(0);
    });
});