Name     : comfortaa-fonts
Version  : 3.001
Release  : 1
URL      : https://orig00.deviantart.net/40a3/f/2017/093/d/4/comfortaa___font_by_aajohan-d1qr019.zip
Source0  : https://orig00.deviantart.net/40a3/f/2017/093/d/4/comfortaa___font_by_aajohan-d1qr019.zip
Summary  : No detailed summary available
Group    : Development/Tools
License  : OFL-1.1

%description
comfortaa fonts

%prep
%setup -n 3.001

%install
install -D -m 0644 Comfortaa-Light.ttf %{buildroot}/usr/share/fonts/X11/TTF/Comfortaa_Thin.ttf
install -D -m 0644 Comfortaa-Regular.ttf %{buildroot}/usr/share/fonts/X11/TTF/Comfortaa_Regular.ttf
install -D -m 0644 Comfortaa-Bold.ttf %{buildroot}/usr/share/fonts/X11/TTF/Comfortaa_Bold.ttf
install -D -m 0644 OFL.txt %{buildroot}/usr/share/licenses/comfortaa-fonts/OFL.txt

%files
%defattr(-,root,root,-)
/usr/share/fonts/X11/TTF/Comfortaa_Thin.ttf
/usr/share/fonts/X11/TTF/Comfortaa_Regular.ttf
/usr/share/fonts/X11/TTF/Comfortaa_Bold.ttf
/usr/share/licenses/comfortaa-fonts/OFL.txt
