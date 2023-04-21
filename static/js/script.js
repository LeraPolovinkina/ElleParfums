const progressBars = document.querySelectorAll('.progress-bar');
progressBars.forEach(progress => {
    const currentElement = progress.querySelector('.current');
    const curValue = progress.getAttribute('data-cur');
    let maxValue = progress.parentElement.getAttribute('data-max');
    const width = (curValue * 100) / maxValue;
    progress.style.width = `${width}%`;
    currentElement.textContent = `${curValue} с.`;
});

progressBars.forEach(progressBar => {
    const spans = progressBar.querySelectorAll('span');
    let totalWidth = 0;

    spans.forEach(span => {
        totalWidth += 20 + span.offsetWidth;
    });

    progressBar.style.minWidth = totalWidth + 'px';
});

(function () {
    document.addEventListener("mousemove", parallax);
    const elem = document.querySelector("#parallax");

    function parallax(e) {
        let _w = window.innerWidth / 2;
        let _h = window.innerHeight / 2;
        let _mouseX = e.clientX;
        let _mouseY = e.clientY;
        let _depth1 = `${50 - (_mouseX - _w) * 0.01}% ${50 - (_mouseY - _h) * 0.01}%`;
        let _depth2 = `${50 - (_mouseX - _w) * 0.02}% ${50 - (_mouseY - _h) * 0.02}%`;
        let _depth3 = `${50 - (_mouseX - _w) * 0.06}% ${50 - (_mouseY - _h) * 0.06}%`;
        let x = `${_depth3}, ${_depth2}, ${_depth1}`;
        console.log(x);
        elem.style.backgroundPosition = x;
    }

})();

