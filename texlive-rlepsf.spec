Name:		texlive-rlepsf
Version:	19082
Release:	2
Summary:	Rewrite labels in EPS graphics
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/generic/rlepsf
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rlepsf.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rlepsf.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
