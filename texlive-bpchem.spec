Name:		texlive-bpchem
Version:	v1.06
Release:	1
Summary:	Typeset chemical names, formulae, etc
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bpchem
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bpchem.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bpchem.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bpchem.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package provides support for typesetting simple chemical
formulae, those long IUPAC compound names, and some chemical
idioms. It also supports the labelling of compounds and
reference to labelled compounds.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    %_texmf_mktexlsr_preun

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mltexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/bpchem/bpchem.sty
%doc %{_texmfdistdir}/doc/latex/bpchem/bpchem.pdf
#- source
%doc %{_texmfdistdir}/source/latex/bpchem/bpchem.dtx
%doc %{_texmfdistdir}/source/latex/bpchem/bpchem.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
