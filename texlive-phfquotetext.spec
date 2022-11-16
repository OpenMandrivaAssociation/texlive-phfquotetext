Name:		texlive-phfquotetext
Version:	41869
Release:	1
Summary:	Quote verbatim text without white space formatting
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/phfquotetext
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/phfquotetext.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/phfquotetext.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/phfquotetext.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides an environment for displaying block text
with special characters, such as verbatim quotes from a referee
report which may contain pseudo-(La)TeX code. This behaves like
a verbatim environment, except that it displays its content as
normal paragraph content, ignoring any white space
preformatting.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/phfquotetext
%{_texmfdistdir}/tex/latex/phfquotetext
%doc %{_texmfdistdir}/doc/latex/phfquotetext

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
