%global tl_name bpchem
%global tl_revision 75878

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	Typeset chemical names, formulae, etc.
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/bpchem
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bpchem.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bpchem.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bpchem.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides support for typesetting simple chemical formulae,
those long IUPAC compound names, and some chemical idioms. It also
supports the labelling of compounds and reference to labelled compounds.

