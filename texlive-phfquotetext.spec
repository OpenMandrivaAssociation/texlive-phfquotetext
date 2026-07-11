%global tl_name phfquotetext
%global tl_revision 41869

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Quote verbatim text without white space formatting
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/phfquotetext
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/phfquotetext.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/phfquotetext.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/phfquotetext.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides an environment for displaying block text with
special characters, such as verbatim quotes from a referee report which
may contain pseudo-(La)TeX code. This behaves like a verbatim
environment, except that it displays its content as normal paragraph
content, ignoring any white space preformatting.

