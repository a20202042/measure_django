$(function () {
    /* Functions */
    var loadForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal .modal-content").html("");
                $("#modal").modal('show');
            },
            success: function (data) {
                $("#modal .modal-content").html(data.html_form);
            }
        });
    };
    var saveForm = function () {
        var form = $(this);
        $.ajax({
            url: form.attr("action"),
            data: form.serialize(),
            type: form.attr("method"),
            dataType: 'json',
            success: function (data) {
                if (data.form_is_valid) {
                    $("#project_table tbody").html(data.html_project_list);
                    $("#modal").modal("hide");
                } else {
                    $("#modal .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };


    /* Binding */

    // Create book
    $(".js-create-project").click(loadForm);
    $("#modal").on("submit", ".js-project-create-form", saveForm);
    //
    // // Update book
    $("#project_table").on("click", ".js-update-project", loadForm);
    $("#modal").on("submit", ".js-project-update-form", saveForm);

    // Delete book
    $("#project_table").on("click", ".js-delet-project", loadForm);
    $("#modal").on("submit", ".js-project-delet", saveForm);


});

$(function () {
    /* Functions */
    var loadForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal .modal-content").html("");
                $("#modal").modal('show');
            },
            success: function (data) {
                $("#modal .modal-content").html(data.html_form);
            }
        });
    };
    var saveForm = function () {
        var form = $(this);
        $.ajax({
            url: form.attr("action"),
            data: form.serialize(),
            type: form.attr("method"),
            dataType: 'json',
            success: function (data) {
                if (data.form_is_valid) {
                    $("#project_item_table tbody").html(data.html_project_item_list);
                    $("#modal").modal("hide");
                } else {
                    $("#modal .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };


    /* Binding */

    // Create book
    // $(".js-create-project").click(loadForm);
    // $("#modal").on("submit", ".js-project-create-form", saveForm);
    //
    // // Update book
    $("#project_item_table").on("click", ".js-update-project-item", loadForm);
    $("#modal").on("submit", ".js-project-item-update-form", saveForm);

    // Delete book
    $("#project_item_table").on("click", ".js-delet-project-item", loadForm);
    $("#modal").on("submit", ".js-project-item-delet", saveForm);


});

$(function () {
    /* Functions */
    var loadForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal .modal-content").html("");
                $("#modal").modal('show');
            },
            success: function (data) {
                $("#modal .modal-content").html(data.html_form);
            }
        });
    };
    var saveForm = function () {
        var form = $(this);
        $.ajax({
            url: form.attr("action"),
            data: form.serialize(),
            type: form.attr("method"),
            dataType: 'json',
            success: function (data) {
                if (data.form_is_valid) {
                    $("#work_order_table tbody").html(data.html_item_list);
                    $("#modal").modal("hide");
                } else {
                    $("#modal .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };


    /* Binding */

    // Create book
    // $(".js-create-project").click(loadForm);
    // $("#modal").on("submit", ".js-project-create-form", saveForm);
    //
    // // Update book
    $("#work_order_table").on("click", ".js-update-project-item", loadForm);
    $("#modal").on("submit", ".js-work_order-update-form", saveForm);

    // Delete book
    $("#work_order_table").on("click", ".js-delet-work-order", loadForm);
    $("#modal").on("submit", ".js-work_order-delet", saveForm);


});
$(function () {
    /* Functions */
    var loadForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal .modal-content").html("");
                $("#modal").modal('show');
            },
            success: function (data) {
                $("#modal .modal-content").html(data.html_form);
            }
        });
    };
    var saveForm = function () {
        var form = $(this);
        $.ajax({
            url: form.attr("action"),
            data: form.serialize(),
            type: form.attr("method"),
            dataType: 'json',
            success: function (data) {
                if (data.form_is_valid) {
                    $("#work_order tbody").html(data.html_work_order_list);
                    $("#modal").modal("hide");
                } else {
                    $("#modal .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };


    /* Binding */

    // Create book
    // $(".js-create-book").click(loadForm);
    // $("#modal-book").on("submit", ".js-book-create-form", saveForm);
    //
    // // Update book
    $("#work_order").on("click", ".js-update-work-order", loadForm);
    $("#modal").on("submit", ".js-work-order-update-form", saveForm);

    // Delete book
    $("#work_order").on("click", ".js-delet-work-order", loadForm);
    $("#modal").on("submit", ".js-work_order-delet", saveForm);

});


$(function () {
    /* Functions */
    var loadForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal .modal-content").html("");
                $("#modal").modal('show');
            },
            success: function (data) {
                $("#modal .modal-content").html(data.html_form);
            }
        });
    };
    var saveForm = function () {
        var form = $(this);
        $.ajax({
            url: form.attr("action"),
            data: form.serialize(),
            type: form.attr("method"),
            dataType: 'json',
            success: function (data) {
                if (data.form_is_valid) {
                    $("#work_order_item_table tbody").html(data.html_item_list);
                    $("#modal").modal("hide");
                } else {
                    $("#modal .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };

    $("#work_order_item_table").on("click", ".js-work_order-item-update", loadForm);
    $("#modal").on("submit", ".js-work_order-item-update-form", saveForm);

    $("#work_order_item_table").on("click", ".js-delet-work_order-item", loadForm);
    $("#modal").on("submit", ".js-work-order-item-delet", saveForm);

});
// --------------------------

$(function () {
    /* Functions */
    var loadForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal .modal-content").html("");
                $("#modal").modal('show');
            },
            success: function (data) {
                $("#modal .modal-content").html(data.html_form);
            }
        });
    };
    var saveForm = function () {
        var form = $(this);
        $.ajax({
            url: form.attr("action"),
            data: form.serialize(),
            type: form.attr("method"),
            dataType: 'json',
            success: function (data) {
                if (data.form_is_valid) {
                    $("#work_order tbody").html(data.html_work_order_list);
                    $("#modal").modal("hide");
                } else {
                    $("#modal .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };


    /* Binding */

    // Create book
    // $(".js-create-book").click(loadForm);
    // $("#modal-book").on("submit", ".js-book-create-form", saveForm);
    //
    // // Update book
    $("#work_order_item_table").on("click", ".js-update-work-order", loadForm);
    $("#modal").on("submit", ".js-work-order-update-form", saveForm);

    // Delete book
    $("#work_order_item_table").on("click", ".js-delet-work-order", loadForm);
    $("#modal").on("submit", ".js-delet-work-order-modal", saveForm);

});

$(function () {
    /* Functions */
    var loadForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal .modal-content").html("");
                $("#modal").modal('show');
            },
            success: function (data) {
                $("#modal .modal-content").html(data.html_form);
            }
        });
    };
    var saveForm = function () {
        var form = $(this);
        $.ajax({
            url: form.attr("action"),
            data: form.serialize(),
            type: form.attr("method"),
            dataType: 'json',
            success: function (data) {
                if (data.form_is_valid) {
                    $("#tool_table tbody").html(data.html_tool_list);
                    $("#modal").modal("hide");
                } else {
                    $("#modal .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };

    $("#tool_table").on("click", ".js-update-tool", loadForm);
    $("#modal").on("submit", ".js-tool-update-form", saveForm);

    $("#tool_table").on("click", ".js-delet-tool", loadForm);
    $("#modal").on("submit", ".js-tool-delet", saveForm);

});


$(function () {
    /* Functions */
    var loadForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal .modal-content").html("");
                $("#modal").modal('show');
            },
            success: function (data) {
                $("#modal .modal-content").html(data.html_form);
            }
        });
    };
    var saveForm = function () {
        var form = $(this);
        $.ajax({
            url: form.attr("action"),
            data: form.serialize(),
            type: form.attr("method"),
            dataType: 'json',
            success: function (data) {
                if (data.form_is_valid) {
                    $("#item_table tbody").html(data.html_item_list);
                    $("#modal").modal("hide");
                } else {
                    $("#modal .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };
    //
    $("#item_table").on("click", ".js-update-item", loadForm);
    $("#modal").on("submit", ".js-item-update-form", saveForm);

    $("#item_table").on("click", ".js-delet-item", loadForm);
    $("#modal").on("submit", ".js-item-delet-modal", saveForm);

});



