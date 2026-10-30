/**
 * navigation.js
 *
 * Handles toggling the navigation menu for small screens and enables tab
 * support for dropdown menus.
 */
( function() {

	var container, button, menu, links, subMenus;

	container = document.getElementById( 'site-navigation' );
	if ( ! container ) {
		return;
	}

	button = container.getElementsByTagName( 'button' )[0];
	if ( 'undefined' === typeof button ) {
		return;
	}

	menu = container.getElementsByTagName( 'ul' )[0];

	// Hide menu toggle button if menu is empty and return early.
	if ( 'undefined' === typeof menu ) {
		button.style.display = 'none';
		return;
	}

	menu.setAttribute( 'aria-expanded', 'false' );
	if ( -1 === menu.className.indexOf( 'nav-menu' ) ) {
		menu.className += ' nav-menu';
	}

	button.onclick = function() {
		if ( -1 !== container.className.indexOf( 'toggled' ) ) {
			container.className = container.className.replace( ' toggled', '' );
			button.setAttribute( 'aria-expanded', 'false' );
			menu.setAttribute( 'aria-expanded', 'false' );
		} else {
			container.className += ' toggled';
			button.setAttribute( 'aria-expanded', 'true' );
			menu.setAttribute( 'aria-expanded', 'true' );
		}
	};

	// Get all the link elements within the menu.
	links    = menu.getElementsByTagName( 'a' );
	subMenus = menu.getElementsByTagName( 'ul' );

	// Set menu items with submenus to aria-haspopup="true".
	for ( var i = 0, len = subMenus.length; i < len; i++ ) {
		subMenus[i].parentNode.setAttribute( 'aria-haspopup', 'true' );
	}

	// Each time a menu link is focused or blurred, toggle focus.
	for ( i = 0, len = links.length; i < len; i++ ) {
		links[i].addEventListener( 'focus', toggleFocus, true );
		links[i].addEventListener( 'blur', toggleFocus, true );
	}

	/**
	 * Sets or removes .focus class on an element.
	 */
	function toggleFocus() {
		var self = this;

		// Move up through the ancestors of the current link until we hit .nav-menu.
		while ( -1 === self.className.indexOf( 'nav-menu' ) ) {

			// On li elements toggle the class .focus.
			if ( 'li' === self.tagName.toLowerCase() ) {
				if ( -1 !== self.className.indexOf( 'focus' ) ) {
					self.className = self.className.replace( ' focus', '' );
				} else {
					self.className += ' focus';
				}
			}

			self = self.parentElement;
		}
	}

	// Fix child menus for touch devices.
	function fixMenuTouchTaps( container ) {
		var touchStartFn,
			parentLink = container.querySelectorAll( '.menu-item-has-children > a, .page_item_has_children > a' );

		if ( 'ontouchstart' in window ) {
			touchStartFn = function( e ) {
				var menuItem = this.parentNode;

				if ( ! menuItem.classList.contains( 'focus' ) ) {
					e.preventDefault();
					for( var i = 0; i < menuItem.parentNode.children.length; ++i ) {
						if ( menuItem === menuItem.parentNode.children[i] ) {
							continue;
						}
						menuItem.parentNode.children[i].classList.remove( 'focus' );
					}
					menuItem.classList.add( 'focus' );
				} else {
					menuItem.classList.remove( 'focus' );
				}
			};

			for ( var i = 0; i < parentLink.length; ++i ) {
				parentLink[i].addEventListener( 'touchstart', touchStartFn, false );
			}
		}
	}

	fixMenuTouchTaps( container );

} )();

/*
 * Dropdown toggles for child menus. Colinear does this with jQuery; this is the same behavior without it,
 * using the screen-reader strings WordPress.com localized for the theme.
 */
( function() {
	var expand = '<span class="screen-reader-text">expand child menu</span>',
		collapse = '<span class="screen-reader-text">collapse child menu</span>';

	document.querySelectorAll( '.main-navigation .menu-item-has-children > a' ).forEach( function( link ) {
		var toggle = document.createElement( 'button' );
		toggle.className = 'dropdown-toggle';
		toggle.setAttribute( 'aria-expanded', 'false' );
		toggle.innerHTML = expand;
		link.insertAdjacentElement( 'afterend', toggle );

		toggle.addEventListener( 'click', function( e ) {
			var subMenu = toggle.nextElementSibling,
				open = toggle.getAttribute( 'aria-expanded' ) === 'false';
			e.preventDefault();
			toggle.classList.toggle( 'toggled' );
			link.classList.toggle( 'toggled' );
			if ( subMenu && subMenu.classList.contains( 'sub-menu' ) ) {
				subMenu.classList.toggle( 'toggled' );
			}
			toggle.setAttribute( 'aria-expanded', open ? 'true' : 'false' );
			toggle.innerHTML = open ? collapse : expand;
		} );
	} );
} )();

/*
 * Sidebar archive dropdown: WordPress printed every month into each page; the static site loads them once.
 */
( function() {
	var select = document.getElementById( 'archives-dropdown-3' );
	if ( ! select ) {
		return;
	}
	var base = select.getAttribute( 'data-base' ) || '';

	fetch( base + '/archives/months.json' )
		.then( function( r ) { return r.json(); } )
		.then( function( months ) {
			months.forEach( function( month ) {
				select.add( new Option( month[1], base + month[0] ) );
			} );
		} );

	select.addEventListener( 'change', function() {
		if ( select.value ) {
			location.href = select.value;
		}
	} );
} )();
