




function Register(){
    var idText = document.querySelector('#registerId').value;
    var passwordText = document.querySelector('#registerPwd').value;
    var emailText = document.querySelector('#registerEmail').value;

    $.ajax({
        url: 'http://127.0.0.1:8000/register/',
        type: 'post',
        data: {
                "userId": `${idText}`,
                "password": `${passwordText}`,
                "email": `${emailText}`
        },
        success: function (data){
            console.log(data)
            alert("데이터전송 성공");
        },
        error: function (error){
            console.log(error)
            alert("에러");
        }
    })
}
document.querySelector("#registerBtn").onclick = Register;