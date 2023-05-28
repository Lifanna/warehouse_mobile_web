import QrScanner from "./qr-scanner.min.js";

$(document).ready(() => {
    const video = document.getElementById('qr-video');
    const videoContainer = document.getElementById('video-container');
    const camHasCamera = document.getElementById('cam-has-camera');
    const camList = document.getElementById('cam-list');
    const camHasFlash = document.getElementById('cam-has-flash');
    const flashToggle = document.getElementById('flash-toggle');
    const flashState = document.getElementById('flash-state');
    const camQrResult = document.getElementById('cam-qr-result');
    const camQrResultTimestamp = document.getElementById('cam-qr-result-timestamp');
    const fileSelector = document.getElementById('file-selector');
    const fileQrResult = document.getElementById('file-qr-result');

    // var product = {}
    // $.ajax({
    //     // url: `/qr/scan_product/${result.data}`,
    //     url: `/qr/scan_product/1`,
    //     method: "GET",
    //     success: (response) => {
    //         product = {
    //             'name': response.name,
    //             'producer': response.producer.name,
    //             'sector': response.sector,
    //             'shelf': response.shelf,
    //             'warehouse': response.warehouse.name,
    //         }
    //         $("#qrForm").html('');
    //         $("#video-container").hide();
    //         var scanningResults = `
    //             <input type="text" class="form-control my-2" placeholder="Наименование" value="${product['name']}">
    //             <input type="text" class="form-control my-2" placeholder="Наименование" value="${product['producer']}">
    //             <input type="text" class="form-control my-2" placeholder="Наименование" value="${product['sector']}">
    //             <input type="text" class="form-control my-2" placeholder="Наименование" value="${product['shelf']}">
    //             <input type="text" class="form-control my-2" placeholder="Наименование" value="${product['warehouse']}">
    //             <div class="d-grid gap-2 my-2">
    //                 <button type="submit" class="my-2 btn btn-block btn-primary" id="scanAgainBtn">Сканировать заново</button>
    //             </div>
    //             <div class="d-grid gap-2 my-2">
    //                 <button type="submit" class="btn btn-block btn-primary" id="takeEquipmentBtn">Взять оборудование</button>
    //             </div>
    //         `
    //         $("#qrForm").append(`<div>${scanningResults}</div>`);
    //     },
    //     error: (error) => {
    //         console.log("Error: ", error)
    //     }
    // })

    $(document).on("click", "#scanAgainBtn", () => {
        $("#qrForm").html('');
        $("#video-container").show();
        scanner.start();
    });

    $(document).on("click", "#scanAgainModalBtn", () => {
        $("#errorModal").modal("hide");
        $("#video-container").show();
        scanner.start();
    });

    $(document).on("click", "#scanAgainNotFoundModalBtn", () => {
        $("#notFoundModal").modal("hide");
        $("#video-container").show();
        scanner.start();
    });

    $(document).on("click", "#takeEquipmentBtn", (event) => {
        $.ajax({
            url: `/equipment/set/${event.currentTarget.attributes["data-equipment"].value}`,
            method: "PATCH",
            data: {
                'id': event.currentTarget.attributes["data-equipment"].value,
                'user': $("#user").val()
            },
            success: (response) => {
                if (response.message == "Оборудование успешно добавлено!") {
                    $("#video-container").hide();
                    $("#successModal").modal("show");
                }
            },
            error: (error) => {
                if (error.status == 404) {
                    $("#video-container").hide();
                    $("#notFoundModal").modal("show");
                    return
                }
                console.log("Error: ", error)
            }
        })
    });

    $(document).on("click", "#scanAgainSuccessModalBtn", () => {
        window.location.href = '/qr/scan';
    });

    $(document).on("click", "#backSuccessModalBtn", () => {
        window.location.href = '/';
    });

    function hasNumber(myString) {
        return /\d/.test(myString);
    }

    function setResult(label, result) {
        var product = {}
        if (!hasNumber(result.data)){
            $("#video-container").hide();
            $("#errorModal").modal("show");
            return
        }
        $.ajax({
            url: `/qr/scan_product/${result.data}`,
            method: "GET",
            success: (response) => {
                product = {
                    'id': response.id,
                    'name': response.name,
                    'producer': response.producer.name,
                    'sector': response.sector,
                    'shelf': response.shelf,
                    'warehouse': response.warehouse.name,
                    'user': response.user
                }
                $("#qrForm").html('');
                $("#video-container").hide();
                if (product['user'] != null) {
                    var takEquipmentBtn = `<button type="button" disabled data-equipment="${product['id']}" 
                    class="btn btn-block btn-primary" id="takeEquipmentBtn">Взять оборудование</button>`
                }
                else {
                    var takEquipmentBtn = `<button type="button" data-equipment="${product['id']}" 
                    class="btn btn-block btn-primary" id="takeEquipmentBtn">Взять оборудование</button>`
                }
                var scanningResults = `
                    <input type="text" class="form-control my-2" readonly value="${product['name']}">
                    <input type="text" class="form-control my-2" readonly value="${product['producer']}">
                    <input type="text" class="form-control my-2" readonly value="${product['sector']}">
                    <input type="text" class="form-control my-2" readonly value="${product['shelf']}">
                    <input type="text" class="form-control my-2" readonly value="${product['warehouse']}">
                    <div class="d-grid gap-2 my-2">
                        <button type="button" class="my-2 btn btn-block btn-primary" id="scanAgainBtn">Сканировать заново</button>
                    </div>
                    <div class="d-grid gap-2 my-2">
                        ${takEquipmentBtn}
                    </div>
                `
                $("#qrForm").append(`<div>${scanningResults}</div>`);
            },
            error: (error) => {
                if (error.status == 404) {
                    $("#video-container").hide();
                    $("#notFoundModal").modal("show");
                    return
                }
                console.log("Error: ", error)
            }
        })
    }


    const scanner = new QrScanner(video, result => setResult(camQrResult, result), {
        onDecodeError: error => {
        },
        highlightScanRegion: true,
        highlightCodeOutline: true,
    });

    scanner.start().then(() => {
        QrScanner.listCameras(true).then(cameras => cameras.forEach(camera => {
            const option = document.createElement('option');
            option.value = camera.id;
            option.text = camera.label;
        }));
    });

    window.scanner = scanner;
});