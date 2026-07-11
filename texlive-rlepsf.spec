%global tl_name rlepsf
%global tl_revision 19082

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Rewrite labels in EPS graphics
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/rlepsf
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/rlepsf.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/rlepsf.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A macro package for use with epsf.tex which allows PostScript labels in
an Encapsulated PostScript file to be replaced by TeX labels. The
package provides commands \relabel (simply replace a PostScript string),
\adjustrelabel (replace a PostScript string, with position adjustment),
and \extralabel (add a label at given coordinates). You can, if you so
choose, use the facilities of the labelfig package in place of using
\extralabel.

