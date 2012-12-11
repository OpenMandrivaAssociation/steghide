Summary:	A steganography program
Name:		steghide
Version:	0.5.1
Release:	%mkrel 13
License:	GPLv2+
Group:		File tools
URL:		http://steghide.sourceforge.net/
Source0:	%{name}-%{version}.tar.bz2
Patch0:		steghide-0.5.1-gcc34.patch
Patch1:		steghide-0.5.1-gcc4.diff
Patch2:		steghide-0.5.1-passphrase-file.diff
Patch3:		steghide-0.5.1-gcc4_1.diff
Patch4:		steghide-0.5.1-libtool.diff
Patch5:		steghide-0.5.1-gcc43.patch
BuildRequires:	autoconf2.5
BuildRequires:	automake
BuildRequires:	doxygen
BuildRequires:	gettext-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libmcrypt-devel >= 2.5.8
BuildRequires:	libmhash-devel
BuildRequires:	libtool
BuildRequires:	libtool-devel
BuildRequires:	zlib-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Steghide is a steganography program which embeds a secret message
in a cover file by replacing some of the least significant bits of
the cover file with bits of the secret message. After that, the
secret message is imperceptible and can only be extracted with the
correct passphrase. To increase invisibility the hidden bits are
encrypted (using the blowfish encryption algorithm) and
pseudo-randomly spreaded in the stego file. Steghide is able to
embed data in BMP, WAV and AU files.

%prep

%setup -q
%patch0 -p0
%patch1 -p1
%patch2 -p1
%patch3 -p0
%patch4 -p1
%patch5 -p1 

%build
rm -f configure
libtoolize --force --copy; aclocal -I m4; autoheader; automake --add-missing --copy --foreign; autoconf
#touch NEWS ChangeLog AUTHORS

%configure2_5x

%make

%check
make check

%install
rm -rf %{buildroot}

%makeinstall_std

# add the html docs
rm -rf html; cp -r doc/doxygen/html .

# fix this
rm -rf %{buildroot}%{_datadir}/doc

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc BUGS CREDITS HISTORY INSTALL README TODO html
%{_bindir}/steghide
%{_mandir}/man1/steghide.1*


%changelog
* Mon Jan 03 2011 Oden Eriksson <oeriksson@mandriva.com> 0.5.1-13mdv2011.0
+ Revision: 627838
- don't force the usage of automake1.7

* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 0.5.1-12mdv2011.0
+ Revision: 614980
- the mass rebuild of 2010.1 packages

* Mon Aug 17 2009 Oden Eriksson <oeriksson@mandriva.com> 0.5.1-11mdv2010.0
+ Revision: 417298
- rebuilt against libjpeg v7

* Tue Jun 23 2009 Jérôme Brenier <incubusss@mandriva.org> 0.5.1-10mdv2010.0
+ Revision: 388123
- rediff P2
- fix license tag

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.5.1-9mdv2009.0
+ Revision: 269368
- rebuild early 2009.0 package (before pixel changes)

* Wed May 21 2008 Oden Eriksson <oeriksson@mandriva.com> 0.5.1-8mdv2009.0
+ Revision: 209739
- added a gcc43 patch from fedora

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.5.1-7mdv2008.1
+ Revision: 136523
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Wed Jan 17 2007 Oden Eriksson <oeriksson@mandriva.com> 0.5.1-7mdv2007.0
+ Revision: 109872
- Import steghide

* Thu Jan 26 2006 Oden Eriksson <oeriksson@mandriva.com> 0.5.1-7mdk
- fix deps

* Thu Jan 26 2006 Oden Eriksson <oeriksson@mandriva.com> 0.5.1-6mdk
- added one gcc4 fix in the debian patch by Gwenole Beauchesne

* Thu Jan 26 2006 Oden Eriksson <oeriksson@mandriva.com> 0.5.1-5mdk
- added one gcc4 patch by Michael Scherer (P3)
- added libtool fixes (P4)

* Sun Jan 08 2006 Oden Eriksson <oeriksson@mandriva.com> 0.5.1-4mdk
- added one gcc4 patch by debian (P1)
- added P2 by Klaus Holler
- fix autofoo
- fix deps
- run the test suite

* Sat Jul 17 2004 Michael Scherer <misc@mandrake.org> 0.5.1-3mdk 
- rebuild for new gcc ( patch 0 )

