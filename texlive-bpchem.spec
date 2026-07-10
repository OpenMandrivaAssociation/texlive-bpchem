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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides support for typesetting simple chemical formulae,
those long IUPAC compound names, and some chemical idioms. It also
supports the labelling of compounds and reference to labelled compounds.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/bpchem
%dir %{_datadir}/texmf-dist/source/latex/bpchem
%dir %{_datadir}/texmf-dist/tex/latex/bpchem
%doc %{_datadir}/texmf-dist/doc/latex/bpchem/README.md
%doc %{_datadir}/texmf-dist/doc/latex/bpchem/bpchem.pdf
%doc %{_datadir}/texmf-dist/source/latex/bpchem/bpchem.dtx
%doc %{_datadir}/texmf-dist/source/latex/bpchem/bpchem.ins
%{_datadir}/texmf-dist/tex/latex/bpchem/bpchem.sty
