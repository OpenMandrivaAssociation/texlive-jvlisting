Name:		texlive-jvlisting
Version:	0.6
Release:	1
Summary:	A replacement for LaTeX's verbatim package
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/jvlisting
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jvlisting.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jvlisting.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jvlisting.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
This package provides a LaTeX environment listing, an
alternative to the built-in verbatim environment. The listing
environment is tailored for including listings of computer
program source code into documents. The main advantages over
the original verbatim environment are: - environments
automatically fixes leading whitespace so that the environment
and program listing can be indented with the rest of the
document source, and; - listing environments may easily be
customised and extended.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/jvlisting/jvlisting.sty
%doc %{_texmfdistdir}/doc/latex/jvlisting/README
%doc %{_texmfdistdir}/doc/latex/jvlisting/examples.tex
%doc %{_texmfdistdir}/doc/latex/jvlisting/jvlisting.pdf
%doc %{_texmfdistdir}/doc/latex/jvlisting/test.tex
#- source
%doc %{_texmfdistdir}/source/latex/jvlisting/jvlisting.dtx
%doc %{_texmfdistdir}/source/latex/jvlisting/jvlisting.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
