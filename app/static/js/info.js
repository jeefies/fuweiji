function r(url) {
	Redirect.RedirectToNewWindow(url);
}

let nowpage = 1;
let maxpage = 3;
let pages = document.getElementsByClassName('Page');

window.onload = function() {
	$('#right').bind('animationend', () => {console.log('set a to 0.6'); $('#right').css('opacity', 0.6)});
	$('#left').bind('animationend', () => {console.log('set a to 0.6');$('#left').css('opacity', 0.6)});
	$('#p1').bind('animationend', () => {console.log('ctx set a to 1');$('#p1').css('opacity', 1)});

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
		if (nowpage == 1) {
			let ar = $('#right');
			let al = $('#left');
			ar.css('opacity', 0.6)
			$('#_nr').css('z-index', 10).css('top', '47.5%')

			al.css('opacity', 0)
			$('#_nl').css('z-index', 5).css('top', '47.5%')
		} else if (nowpage == maxpage) {
			let ar = $('#right');
			let al = $('#left');
			al.css('opacity', 0.6)
			$('#_nl').css('z-index', 10).css('top', '47.5%')

			ar.css('opacity', 0)
			$('#_nr').css('z-index', 5).css('top', '47.5%')
		} else {
			console.log('??')
			let ar = $('#right').css('opacity', 0.6);
			let al = $('#left').css('opacity', 0.6);

			$('#_nr').css('top', '44.5%');
			$('#_nl').css('top', '50.5%');
		}
	}

	$('#right').bind('click', () => nextpagefunc(1));
	$('#left').bind('click', () => nextpagefunc(-1))
}
