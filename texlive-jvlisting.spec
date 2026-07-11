%global tl_name jvlisting
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.7
Release:	%{tl_revision}.1
Summary:	A replacement for LaTeXs verbatim package
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/jvlisting
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/jvlisting.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/jvlisting.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/jvlisting.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides a LaTeX environment listing, an alternative to the
built-in verbatim environment. The listing environment is tailored for
including listings of computer program source code into documents. The
main advantages over the original verbatim environment are: environments
automatically fixes leading whitespace so that the environment and
program listing can be indented with the rest of the document source,
and; listing environments may easily be customised and extended.

