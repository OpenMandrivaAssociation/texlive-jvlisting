# revision 24638
# category Package
# catalog-ctan /macros/latex/contrib/jvlisting
# catalog-date 2011-11-18 01:15:46 +0100
# catalog-license lppl
# catalog-version 0.7
Name:		texlive-jvlisting
Version:	0.7
Release:	2
Summary:	A replacement for LaTeX's verbatim package
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/jvlisting
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jvlisting.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jvlisting.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jvlisting.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

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

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.7-2
+ Revision: 752941
- Rebuild to reduce used resources

* Fri Dec 09 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.7-1
+ Revision: 739795
- texlive-jvlisting

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.6-1
+ Revision: 718765
- texlive-jvlisting
- texlive-jvlisting
- texlive-jvlisting
- texlive-jvlisting

