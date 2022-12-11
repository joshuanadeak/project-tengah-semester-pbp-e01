
    function getFormData($form) {
        var unindexed_array = $form.serializeArray();
    var indexed_array = { };

    $.map(unindexed_array, function (n, i) {
        indexed_array[n['name']] = n['value'];
        });

    return indexed_array;
    }

    function displayStock(json){
        console.log(json)
        var button = (pk) => `<button onclick="deleteStock(${pk})" class="btn btn-outline-danger btn-sm rounded-pill">SELL</button>`
    $("#stock-table").empty()
    for(var i = 0 ;i < json.length ; i++){
        console.log("ini fie")
            console.log(json[i].fields)
    $("#stock-table").append("<tr><td>" + json[i].fields.kode_saham+"</td><td>"+ json[i].fields.nama_perusahaan+"</td><td>"+ json[i].fields.harga_saham+"</td><td style='color: rgb(4, 169, 4); font-weight: bold'>"+ json[i].fields.risk+"</td><td>"+button(json[i].pk)+"</td></tr>")
        }
    }

    function displayNote(json) {
        console.log("INI MASUK DISPLAY NOTEE")
        console.log(json)
    $("#personal-note").text(json[0].fields.catatan)
    }

    function updateStock() {
        $.getJSON("/stock/json", displayStock);
    }

    function deleteStock(pk) {
        console.log(pk)
        $.ajax({
        url: `/stock/delete_stock/${pk}`,
    type: 'post',
    data: { },
    success: function(){
        updateStock(),
        $("#sellModal").modal('show');
            }
        });
    }

    $(document).ready(function () {
        $.getJSON("/stock/json", displayStock);
    $.getJSON("/stock/porto/njson", displayNote);
    console.log("notenote")
    document.getElementById("modalButton").setAttribute('onclick', '$("#formModal").modal("show")');

    $("#addTaskForm").submit(function (e) {
        e.preventDefault();
    $(".btnClick").prop('disabled', true);
    $(".btnClick").text('Processing...');
    var $form = $(this);
    var serializedData = getFormData($form);

    console.log("BELOM MASUK AJAX")
    $.ajax({
        url: "/stock/porto/add_note/",
    type: "POST",
    data: serializedData,
    dataType: 'text',
    success: function (response_data) {
        console.log("ENTERRRR")
                    $(".btnClick").prop('disabled', false);
    $(".btnClick").text('Submit');

    $.getJSON("/stock/porto/njson",
    displayNote);

    $("#formModal").modal('hide');
    $('#addTaskForm').each(function () {
        this.reset();
                    });
                }
            });
        });
    });
