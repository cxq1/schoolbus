//计算坐标函数
var Mouse = function(e) {
	mouse = new MouseEvent(e);
	return mouse;
}
//获取鼠标坐标函数
var MouseEvent = function(e) {
	this.x = e.pageX
	this.y = e.pageY
}

/* 检查密码安全度  */
function checkPwdRank(e, a, d) {
	var b = $(e);
	var c = b.val();
	if(c.length <= 6 || new RegExp("^[a-zA-Z]{6,}$").test(c) || new RegExp("^[0-9]{6,}$").test(c) || new RegExp("^[_]{6,}$").test(c)) {
		$("#" + a).attr("title", "危险");
		$("#" + d).html("危险");
		$("#" + a).removeClass("rank-a");
		$("#" + a).removeClass("rank-b");
		$("#" + a).removeClass("rank-c");
		$("#" + a).addClass("rank-a")
	} else {
		if(c.length > 6 && new RegExp("[a-zA-Z]").test(c) && new RegExp("[0-9]").test(c) && new RegExp("[_]").test(c)) {
			$("#" + a).attr("title", "安全");
			$("#" + d).html("安全");
			$("#" + a).removeClass("rank-a");
			$("#" + a).removeClass("rank-b");
			$("#" + a).removeClass("rank-c");
			$("#" + a).addClass("rank-c")
		} else {
			$("#" + a).attr("title", "一般");
			$("#" + d).html("一般");
			$("#" + a).removeClass("rank-a");
			$("#" + a).removeClass("rank-b");
			$("#" + a).removeClass("rank-c");
			$("#" + a).addClass("rank-b")
		}
	}
}

/*  检查密码类型   */
function checkFormat(data) {
	var type = 0;
	var isNum = false;
	var isLetter = false;
	var isSymbol = false;
	var numreg = /[0-9]/;
	var letterreg = /[a-zA-Z]/;
	for(var i = 0; i < data.length; i++) {
		if(!isNum && numreg.test(data[i])) { //为数字
			isNum = true;
			type++;
		} else if(!isLetter && letterreg.test(data[i])) { //为字母
			isLetter = true;
			type++;
		} else if(!isSymbol && data[i] == '_') {
			isSymbol = true;
			type++;
		}
	}
	return type;
}

/*  身份证浮出框  */
function cardShow() {
	var k = $("#cardCode").val();
	if(k != "") {
		var j = "";
		var h = k.length;
		if(k.length <= 3) {
			j = k
		} else {
			if(h <= 6) {
				j = k.substring(0, 3) + " " + k.substring(3, h)
			} else {
				j = k.substring(0, 3) + " " + k.substring(3, 6) + "  " + k.substring(6, 14) + " " + k.substring(14, h)
			}
		}
		$("#cardCode_div").html(j);
		$("#cardCode_div").show();
		if($("#cardType").val() == "0") {
			if(k.length == 18) {
				var i = k.substring(6, 10);
				var g = k.substring(10, 12);
				var f = k.substring(12, 14);
				var e = i + "-" + g + "-" + f;
				$("#born_date").val(e)
			}
		}
	} else {
		$("#cardCode_div").html("");
		$("#cardCode_div").hide()
	}
}