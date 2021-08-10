class Redirect {

	Redirect(url) {
		this.url = url;
		this.Redirect = () => Redirect.RedirectUrl(this.url);
		this.RedirectToNewWindow = () => Redirect.RedirectToNewWindow(this.url);
	}


	static RedirectUrl(url) {
		console.log("RedirectUrl");
		location.href = url;
	}

	static RedirectAssign(url) {
		console.log("RedirectAssign");
		location.assign(url);
	}

	static RedirectReplace(url) {
		console.log("RedirectReplace");
		location.replace(url);
	}

	// 其他的结果都是一样的,只有这一个方法会新建一个窗口
	static RedirectToNewWindow(url) {
		console.log("RedirectToNewWindow");
		window.open(url);
	}
}
