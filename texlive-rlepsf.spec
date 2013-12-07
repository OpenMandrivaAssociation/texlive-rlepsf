# revision 19082
# category Package
# catalog-ctan /macros/generic/rlepsf
# catalog-date 2007-01-13 23:45:25 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-rlepsf
Version:	20070113
Release:	6
Summary:	Rewrite labels in EPS graphics
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/generic/rlepsf
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rlepsf.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rlepsf.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A macro package for use with epsf.tex which allows PostScript
labels in an Encapsulated PostScript file to be replaced by TeX
labels. The package provides commands \relabel (simply replace
a PostScript string), \adjustrelabel (replace a PostScript
string, with position adjustment), and \extralabel (add a label
at given coordinates). You can, if you so choose, use the
facilities of the labelfig package in place of using
\extralabel.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/rlepsf/rlepsf.tex
%doc %{_texmfdistdir}/doc/generic/rlepsf/read.me
%doc %{_texmfdistdir}/doc/generic/rlepsf/rlepsdoc.ps

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20070113-2
+ Revision: 755684
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20070113-1
+ Revision: 719455
- texlive-rlepsf
- texlive-rlepsf
- texlive-rlepsf
- texlive-rlepsf

