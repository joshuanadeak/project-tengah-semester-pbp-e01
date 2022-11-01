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
        var button = (pk) => `<button onclick="deleteStock(${pk})" class="btn btn-outline-success rounded-pill btn-sm">BUY</button>`
    $("#market-table").empty()
    for(var i = 0 ;i < json.length ; i++){
        console.log("ini fie")
            console.log(json[i].fields)
    $("#market-table").append("<tr><td>" + json[i].fields.kode_saham+"</td><td>"+ json[i].fields.nama_perusahaan+"</td><td>"+ json[i].fields.harga_saham+"</td><td style='color: rgb(4, 169, 4); font-weight: bold' >"+ json[i].fields.risk+"</td><td>"+button(json[i].pk)+"</td></tr>")
        }
    }

    function updateStock() {
        $.getJSON("/stock/mjson", displayStock);
    }

    function deleteStock(pk) {
        console.log(pk)
        $.ajax({
        url: `/stock/delete_market/${pk}`,
    type: 'post',
    data: { },
    success: function(){
        updateStock(),
        $("#buyModal").modal('show');
            }
        });
    }

    $(document).ready(function () {
        $.getJSON("/stock/mjson", displayStock);
    document.getElementById("modalButton").setAttribute('onclick', '$("#formModal").modal("show")');
    console.log("SEBELOM SUBMIT")
    $("#addTaskForm").submit(function (e) {
        e.preventDefault();
    $(".btnClick").prop('disabled', true);
    $(".btnClick").text('Processing...');
    var $form = $(this);
    var serializedData = getFormData($form);

    $.ajax({
        url: "/stock/add/",
    type: "POST",
    data: serializedData,
    dataType: 'text',
    success: function (response_data) {
        console.log(response_data)
                    $(".btnClick").prop('disabled', false);
    $(".btnClick").text('Submit');
    $.getJSON("/stock/mjson",
    displayStock);

    $("#formModal").modal('hide');
    $('#addTaskForm').each(function () {
        this.reset();
                    });
                    
                }
            });
        });
    });
