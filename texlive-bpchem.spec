Name:		texlive-bpchem
Version:	45120
Release:	1
Summary:	Typeset chemical names, formulae, etc
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bpchem
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bpchem.r45120.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bpchem.doc.r45120.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bpchem.source.r45120.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides support for typesetting simple chemical
formulae, those long IUPAC compound names, and some chemical
idioms. It also supports the labelling of compounds and
reference to labelled compounds.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/bpchem/bpchem.sty
%doc %{_texmfdistdir}/doc/latex/bpchem/bpchem.pdf
%doc %{_texmfdistdir}/doc/latex/bpchem/README.md
#- source
%doc %{_texmfdistdir}/source/latex/bpchem/bpchem.dtx
%doc %{_texmfdistdir}/source/latex/bpchem/bpchem.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
