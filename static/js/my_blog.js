// Changes innertext on summary tag when user open and close blog post content
/* jshint esversion: 6 */
$(document).ready(function () {

    $('details').click(function () {
        let summary = this.querySelector(".post-detail-summary");

        if (this.hasAttribute('open')) {
            summary.innerText = 'Show More';
        } else {
            summary.innerText = 'Close';
        }
    });

});