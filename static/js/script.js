function randomInRange(min, max) {
    return Math.random() * (max - min) + min;
}

function randomOneZero() {
    let items = [0, 0, 0, 0, 1]
    return items[Math.floor(Math.random() * items.length)];
}

let pizza_was_or_not = false
const progressBars = document.querySelectorAll('.progress-bar');
let suc_color = ''

const xhr = new XMLHttpRequest();
xhr.open('GET', 'update/');
xhr.onload = function () {
    if (xhr.status === 200) {
        const response = JSON.parse(xhr.responseText);
        suc_color = response['variable']["success_color"];
        progressBars.forEach(progress => {
            const texts = progress.querySelectorAll('span')
            const currentElement = progress.querySelector('.current');
            const curValue = progress.getAttribute('data-cur');
            let maxValue = progress.parentElement.getAttribute('data-max');
            const width = (curValue * 100) / maxValue;
            if (width >= 100) {
                progress.style.backgroundColor = suc_color
                texts.forEach(text => {
                    text.style.color = '#FFF'
                })
                progress.style.width = `${width}%`;
            } else {
                progress.style.width = `${width + (30 - (30 * width / 100))}%`;
            }
            currentElement.textContent = `${curValue}`;
        });
    } else {
        console.log('Request failed.  Returned status of ' + xhr.status);
    }
};
xhr.send();

progressBars.forEach(progressBar => {
    const spans = progressBar.querySelectorAll('span');
    let totalWidth = 0;

    spans.forEach(span => {
        totalWidth += 25 + span.offsetWidth;
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
        elem.style.backgroundPosition = x;
    }

})();

// Функция для выполнения AJAX-запроса и обновления данных на странице
function updateData() {
    $.ajax({
        url: 'update/', // URL
        type: 'GET', // Метод HTTP-запроса
        dataType: 'json', // Ожидаемый формат данных в ответе
        success: function (data) {

            console.log(data)
            var users_s = JSON.parse(data['users'])
            var variable = data['variable']
            var today = data['today']
            var month = data['month']
            // Функция обработки успешного ответа от сервера
            // Очистка текущего списка пользователей на странице
            $('#user-list').empty();

            // Добавление каждого пользователя из полученных данных на страницу
            $.each(users_s, function (index, user) {
                if (index === 0) {
                    // Создаем HTML-код с данными пользователя
                    var userHtml = '<div class="progress mb-4" data-max="' + user['fields']['goal'] + '" style="height: 2.5rem;">' +
                        '<div class="progress-bar d-flex flex-row justify-content-between px-3" role="progressbar" ' +
                        'data-cur="' + user['fields']['profit'] + '" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100">' +
                        '<span class="float-end"><img src="/static/img/1f947.png" class="empl-medal" alt="">' + user['fields']['name'] + '</span>' +
                        '<span class="current float-end">' + user['fields']['profit'] + ' </span>' +
                        '</div>' +
                        '</div>';
                } else {
                    // Создаем HTML-код с данными пользователя
                    var userHtml = '<div class="progress mb-4" data-max="' + user['fields']['goal'] + '" style="height: 2.5rem;">' +
                        '<div class="progress-bar d-flex flex-row justify-content-between px-3" role="progressbar" ' +
                        'data-cur="' + user['fields']['profit'] + '" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100">' +
                        '<span class="float-end">' + user['fields']['name'] + '</span>' +
                        '<span class="current float-end">' + user['fields']['profit'] + ' </span>' +
                        '</div>' +
                        '</div>';
                }

                // Вставляем созданный HTML-код в нужное место на странице
                $('#user-list').append(userHtml);
            });


            // Получаем элемент, который нужно изменить
            let progressBlock = $('.progress-block');
            progressBlock.empty()
            // Изменяем содержимое элемента
            progressBlock.append(`
                <div class="progress-circle ${month['percent'] > 50 ? 'over50' : ''} p${month['percent']} m-0">
                    <span class="d-flex flex-column justify-content-center">
                        <h1 class="circle-h1">${month['profit']}</h1>
                        <h5 class="circle-sub">GOAL ${variable['global_goal']}</h5>
                        <div class="emoji-circle">
                                <img style="height: 2.5rem" 
                                                           src="static/img/tango.png" alt="">
                                <img
                                    style="height: 2.5rem" src="static/img/beer.png" alt="">
                            </div>
                    </span>
                    <div class="left-half-clipper">
                        <div class="first50-bar"></div>
                        <div class="value-bar"></div>
                    </div>
                </div>
            `);

            let progress_day = $('#progress_day');
            let curValue_day = progress_day.find('.progress-bar').data('cur');
            progress_day.empty()
            progress_day.append(`
                <div class="progress mb-4" data-max="${variable['today_goal']}" style="height: 2.5rem;">
                    <div class="progress-bar d-flex flex-row justify-content-between px-3" role="progressbar"
                            data-cur="${today['profit']}">
                        <span class="current m-0">${today['profit']}</span>
                    </div>
                </div>
            `);
            const progressBars = document.querySelectorAll('.progress-bar');
            progressBars.forEach(progress => {
                const currentElement = progress.querySelector('.current');
                const curValue = progress.getAttribute('data-cur');
                let maxValue = progress.parentElement.getAttribute('data-max');
                const width = (curValue * 100) / maxValue;
                const texts = progress.querySelectorAll('span');
                if (width >= 100) {
                    progress.style.backgroundColor = variable['success_color'];
                    texts.forEach(text => {
                        text.style.color = '#FFF'
                    })
                    progress.style.width = `${width}%`;
                } else {
                    progress.style.width = `${width + (30 - (30 * width / 100))}%`;
                }
                currentElement.textContent = `${curValue}`;
            });

            progressBars.forEach(progressBar => {
                const spans = progressBar.querySelectorAll('span');
                let totalWidth = 0;

                spans.forEach(span => {
                    totalWidth += 25 + span.offsetWidth;
                });

                progressBar.style.minWidth = totalWidth + 'px';
            });
            if (today['profit'] >= variable['today_goal'] && !pizza_was_or_not) {
                pizza_was_or_not = true
                const end = Date.now() + 10 * 1000;

                const audio = new Audio('static/sounds/pizza.mp3');
                audio.play().then(r => {});
                (function frame() {
                    confetti({
                        particleCount: randomOneZero(),
                        angle: 60,
                        spread: 55,
                        origin: {x: 0},
                        scalar: randomInRange(4, 7),
                        shapes: ["image"],
                        shapeOptions: {
                            image: [
                                {
                                    src: "static/img/pizza.png",
                                    width: 32,
                                    height: 32,
                                },
                            ],
                        },
                    });

                    confetti({
                        particleCount: randomOneZero(),
                        angle: 120,
                        spread: -55,
                        origin: {x: 1},
                        scalar: randomInRange(4, 7),
                        shapes: ["image"],
                        shapeOptions: {
                            image: [
                                {
                                    src: "static/img/pizza.png",
                                    width: 32,
                                    height: 32,
                                },
                            ],
                        },
                    });

                    if (Date.now() < end) {
                        requestAnimationFrame(frame);
                    }
                })();
            }
            if (curValue_day < today['profit']) {
                const audio = new Audio('static/sounds/sale.mp3');
                audio.play().then(r => {});
                const duration = 10 * 1000,
                    animationEnd = Date.now() + duration,
                    defaults = {startVelocity: 30, spread: 360, ticks: 60, zIndex: 0};

                const interval = setInterval(function () {
                    const timeLeft = animationEnd - Date.now();

                    if (timeLeft <= 0) {
                        return clearInterval(interval);
                    }

                    const particleCount = 50 * (timeLeft / duration);

                    // since particles fall down, start a bit higher than random
                    confetti(
                        Object.assign({}, defaults, {
                            particleCount,
                            origin: {x: randomInRange(0.1, 0.3), y: Math.random() - 0.2},
                        })
                    );
                    confetti(
                        Object.assign({}, defaults, {
                            particleCount,
                            origin: {x: randomInRange(0.7, 0.9), y: Math.random() - 0.2},
                        })
                    );
                }, 250);
            }
        },
        error: function (xhr, textStatus, errorThrown) {
            // Функция обработки ошибок AJAX-запроса
            console.error('Ошибка при выполнении AJAX-запроса: ' + textStatus + ', ' + errorThrown);
        }
    });
}
