
function displayFieldErr(field, err_msgs) {
    console.log("---displayFieldErr--");
    if (document.getElementById(field)) {
        document.getElementById(field).style.border = "2px solid red";
        document.getElementById(field + "_err").innerHTML = err_msgs;
    } else if (document.getElementById(field + "_err")) {
        document.getElementById(field + "_err").innerHTML = err_msgs;
    }
}

function onFieldTypeHandle(x, key) {
    if (document.getElementById(key)) {
        document.getElementById(key).style.border = null;
        document.getElementById(key + "_err").innerHTML = null;
    } else if (document.getElementById(key + "_err")) {
        document.getElementById(key + "_err").innerHTML = null;
    }
}


function clearFieldErr() {
    $(".form-control").css("border", "1px solid #dee2e6");
    $(".form-err-msg").text("");
}


function showAlert(key, msg) {
    document.getElementById(key + "-msg").innerHTML = msg;
    $('#' + key).show();
    $("#" + key).fadeTo(3000, 500).slideUp(500, function () {
        $("#" + key).slideUp(500);
    });
}
function hideAlert(key) {
    $('#' + key).hide();
}


function handleApiResp(apiResp) {
    let result = false;
    try {
        if (apiResp["status_code"] == 200) {
            onFieldTypeHandle(this, "non_field_errors");
            showAlert("success-alert", apiResp["message"][0]);
            result = true;
        } else {
            Object.entries(apiResp["message"]).forEach(([field, err_li]) => {
                console.log("The field: ", field);
                console.log("The err_li: ", err_li);
                let err_msgs = "";
                for (err of err_li) {
                    console.log("---err: ", err);
                    err_msgs += err + "<br>";
                }
                displayFieldErr(field, err_msgs);
            })
            showAlert("error-alert", "Invalid form data!!!");
        }
    } catch (err) {
        console.log("---EXCEPTION--handleApiResp--", err)
    } finally {
        return result;
    }
}


function redirect_to(url_path) {
    window.location = url_path;
}
