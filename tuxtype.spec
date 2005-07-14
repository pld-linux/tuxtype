Summary:	Tux Typing - Graphical, educational typing tutorial game
Summary(pl):	Tux Typing - Gra edukacyjna, ucz±ca pisania na klawiaturze
Name:		tuxtype
Version:	1.0.3
Release:	2
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/tuxtype/%{name}-%{version}.tar.bz2
# Source0-md5:	a86bccdf9d75c98b17ebf1ee03f56b76
Source1:	%{name}.desktop
Patch0:		%{name}-Makefile.patch
Patch1:		%{name}-ac-am.patch
URL:		http://www.geekcomix.com/dm/tuxtype/
BuildRequires:	SDL-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_image-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Educational typing tutor starring Tux, the Linux Penguin. Object of
the game is to catch fish as they drop from the top of the screen.
Each fish has a letter or a word written on it, and Tux eats the fish
by the player pressing the associated key or typing the appropriate
word. Intended to be cute and fun for children learning to type and
spell.

%description -l pl
Nauka pisania z Tuksem, linuksowym pingwinem w roli g³ównej. Celem
gry jest ³apanie rybek spadaj±cych z góry ekranu. Na ka¿dej rybce
napisana jest litera lub s³owo, a Tux zjada rybkê gdy gracz naci¶nie
odpowiedni klawisz, b±d¼ wpisze w³a¶ciwe s³owo. Gra zosta³a pomy¶lana
by byæ mi³ym sposobem nauki pisania na klawiaturze dla dzieci.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

:> acinclude.m4

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR="$RPM_BUILD_ROOT"

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README AUTHORS TODO tuxtype/*/*.TXT* tuxtype/docs/en/*.html
%attr(755,root,root) %{_bindir}/*
%{_datadir}/tuxtype
%{_desktopdir}/*.desktop
