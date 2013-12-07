# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/bpchem
# catalog-date 2006-12-01 14:16:52 +0100
# catalog-license lppl
# catalog-version v1.06
Name:		texlive-bpchem
Version:	v1.06
Release:	6
Summary:	Typeset chemical names, formulae, etc
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bpchem
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bpchem.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bpchem.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bpchem.source.tar.xz
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


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> v1.06-2
+ Revision: 749881
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> v1.06-1
+ Revision: 717978
- texlive-bpchem
- texlive-bpchem
- texlive-bpchem
- texlive-bpchem
- texlive-bpchem

