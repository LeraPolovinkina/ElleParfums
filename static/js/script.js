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
                // Создаем HTML-код с данными пользователя
                var userHtml = '<div class="progress mb-4" data-max="' + variable['employee_goal'] + '" style="height: 2.5rem;">' +
                    '<div class="progress-bar d-flex flex-row justify-content-between px-3" role="progressbar" ' +
                    'data-cur="' + user['fields']['profit'] + '" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100">' +
                    '<span class="float-end">' + user['fields']['name'] + '</span>' +
                    '<span class="current float-end">' + user['fields']['profit'] + ' c.</span>' +
                    '</div>' +
                    '</div>';
                // Вставляем созданный HTML-код в нужное место на странице
                $('#user-list').append(userHtml);
            });

            console.log('gg');

            // Получаем элемент, который нужно изменить
            let progressBlock = $('.progress-block');
            progressBlock.empty()
            // Изменяем содержимое элемента
            progressBlock.append(`
                <div class="progress-circle ${month['percent'] > 50 ? 'over50' : ''} p${month['percent']} m-0">
                    <span class="d-flex flex-column justify-content-center">
                        <h1 class="circle-h1">${month['profit']}</h1>
                        <h5 class="circle-sub">GOAL ${variable['global_goal']}</h5>
                    </span>
                    <div class="left-half-clipper">
                        <div class="first50-bar"></div>
                        <div class="value-bar"></div>
                    </div>
                </div>
            `);

            let progress_day = $('#progress_day');
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

        },
        error: function (xhr, textStatus, errorThrown) {
            // Функция обработки ошибок AJAX-запроса
            console.error('Ошибка при выполнении AJAX-запроса: ' + textStatus + ', ' + errorThrown);
        }
    });
}
