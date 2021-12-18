function r(url) {
	Redirect.RedirectToNewWindow(url);
}

let nowpage = 1;
let pages = document.getElementsByClassName('Page');
let maxpage = 0;

window.onload = function() {
	maxpage = pages.length;
	tidyPages();

	$('#right').bind('animationend', () => {
		console.log('set a to 0.6'); 
		$('#right').css('opacity', 0.6)
	});
	$('#left').bind('animationend', () => {
		console.log('set a to 0.6');
		$('#left').css('opacity', 0.6)
	});
	$('#p1').bind('animationend', () => {
		console.log('ctx set a to 1');
		$('#p1').css('opacity', 1)
	});

	let nextpagefunc = function(next) {
		console.log('next page clicked', next)
		let i = nowpage
		if ((nowpage >= maxpage && next == 1) || (next == -1 && nowpage == 0)) {
			alert('No page anymore');
			return
		}
		let p1 = $('div.Page#p' + i).css('animation-name', 'hide')
		p1.bind('animationend', () => p1.css('opacity', 0));
		
		console.log('div.Page#p' + i);
		i += next;

		let p2 = $('div.Page#p' + i).css('animation-name', 'show')
		p2.bind('animationend', () => p2.css('opacity', 1));

		console.log('div.Page#p' + i);

		nowpage += next;
		if (nowpage <= 1) {
			let ar = $('#right');
			let al = $('#left');
			ar.css('opacity', 0.6)
			$('#_nr').css('z-index', 10).css('top', '47.5%')

			al.css('opacity', 0)
			$('#_nl').css('z-index', 5).css('top', '47.5%')

			nowpage = 1
		} else if (nowpage >= maxpage) {
			let ar = $('#right');
			let al = $('#left');
			al.css('opacity', 0.6)
			$('#_nl').css('z-index', 10).css('top', '47.5%')

			ar.css('opacity', 0)
			$('#_nr').css('z-index', 5).css('top', '47.5%')

			nowpage = maxpage;
		} else {
			let ar = $('#right').css('opacity', 0.6);
			let al = $('#left').css('opacity', 0.6);

			$('#_nr').css('top', '44.5%');
			$('#_nl').css('top', '50.5%');
		}
	}

	$('#right').bind('click', () => nextpagefunc(1));
	$('#left').bind('click', () => nextpagefunc(-1))
}

function tidyPages() {
	for (let i = 0; i < maxpage; i++) {
		console.log(pages[i].innerHTML);
		tidyPage(i)
	}
}

function tidyPage(i) {
	console.log("Tidying")
	let page = pages[i];
	let ctx = page.innerHTML.trim();

	// Replace all lines
	ctx = ctx.split('\n').map((x) => x.trim()).join('\n');
	ctx = ctx.replace(/\n\n/g, '</p><br /><p>').split('\n')
	ctx = "<p>" + ctx.join("</p>\n<p>") + "</p>"

	// Add quoted contents
	let octx  = ctx.split('<p>"""</p>')
	ctx =  octx[0]
	let sep = ["<div class='quoted'>", "</div>"]
	for (let i = 1; i < octx.length; i++) {
		console.log(i)
		ctx += sep[(i - 1) % 2] + octx[i]
	}

	ctx = ctx.replace(/\[(.*?)\]\((.*?)\)/g, "<span class='jump' onclick=\"r('$2')\">$1</span>")
	ctx = ctx.replace(/\((.*?)\)\[(.*?)\]/g, "<span class='jump' onclick=\"r('$1')\">$2</span>")
	console.log(ctx);

	page.innerHTML = ctx;

}
