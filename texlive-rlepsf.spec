# revision 19082
# category Package
# catalog-ctan /macros/generic/rlepsf
# catalog-date 2007-01-13 23:45:25 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-rlepsf
Version:	20070113
Release:	1
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
A macro package for use with epsf.tex which allows PostScript
labels in an Encapsulated PostScript file to be replaced by TeX
labels. The package provides commands \relabel (simply replace
a PostScript string), \adjustrelabel (replace a PostScript
string, with position adjustment), and \extralabel (add a label
at given coordinates). You can, if you so choose, use the
facilities of the labelfig package in place of using
\extralabel.

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
%{_texmfdistdir}/tex/generic/rlepsf/rlepsf.tex
%doc %{_texmfdistdir}/doc/generic/rlepsf/read.me
%doc %{_texmfdistdir}/doc/generic/rlepsf/rlepsdoc.ps
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
