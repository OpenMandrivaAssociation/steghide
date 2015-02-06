%define debug_package %{nil}

Summary:	A steganography program
Name:		steghide
Version:	0.5.1
Release:	15
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
BuildRequires:	jpeg-devel
BuildRequires:	libmcrypt-devel >= 2.5.8
BuildRequires:	mhash-devel
BuildRequires:	libtool
BuildRequires:	libtool-devel
BuildRequires:	zlib-devel

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
%makeinstall_std

# add the html docs
rm -rf html; cp -r doc/doxygen/html .

# fix this
rm -rf %{buildroot}%{_datadir}/doc

%find_lang %{name}

%files -f %{name}.lang
%doc BUGS CREDITS HISTORY INSTALL README TODO html
%{_bindir}/steghide
%{_mandir}/man1/steghide.1*
