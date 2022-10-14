Name:           atomes
Version:        1.1.7
Release:        8%{?dist}
Summary:        An atomistic toolbox
License:        AGPL-3.0-or-later
Source0:        https://github.com/Slookeur/Atomes-rpm-build/raw/main/%{name}-%{version}.tar.gz
Source1:        https://github.com/Slookeur/Atomes-rpm-build/raw/main/%{name}-%{version}.tar.gz.asc
Source2:        %{name}.gpg
URL:            https://%{name}.ipcms.fr/

BuildRequires: gnupg2
BuildRequires: make
BuildRequires: automake
BuildRequires: autoconf
BuildRequires: gcc
BuildRequires: gcc-gfortran
BuildRequires: libgfortran
BuildRequires: gtk3-devel
BuildRequires: libxml2-devel
BuildRequires: freeglut-devel
BuildRequires: mesa-libGLU-devel
BuildRequires: libepoxy-devel
BuildRequires: ffmpeg-devel
BuildRequires: desktop-file-utils

# For Suse-based linux
%if 0%{?suse_version}
BuildRequires: update-desktop-files
%endif
 
Requires: gtk3
#Requires: libgfortran
# Requires: libxml2
Requires: ffmpeg-libs
Requires: freeglut
Requires: mesa-libGLU
# Requires: libepoxy
Requires: desktop-file-utils
Requires: bash-completion

Provides: %{name} = %{version}-%{release}

%description
Atomes: a toolbox to analyze, to visualize 
and to create/edit three-dimensional atomistic models.
It offers a workspace that allows to have many projects opened simultaneously.
The different projects in the workspace can exchange data: 
analysis results, atomic coordinates...
Atomes also provides an advanced input preparation system 
for further calculations using well known molecular dynamics codes:

    Classical MD: DLPOLY and LAMMPS
    ab-initio MD: CPMD and CP2K
    QM-MM MD: CPMD and CP2K

To prepare the input files for these calculations is likely to be the key, 
and most complicated step towards MD simulations.
Atomes offers a user-friendly assistant to help and guide the scientist
step by step to achieve this crucial step.

%prep
# %%{gpgverify} --keyring='%%{SOURCE2}' --signature='%%{SOURCE1}' --data='%%{SOURCE0}'
%autosetup

%build
%configure --prefix=/usr
make `%{?_smp_mflags}`

%install
%make_install

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop

%files
%license COPYING
%{_bindir}/%{name}
%{_datadir}/doc/%{name}/
%{_datadir}/%{name}/
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/%{name}.1.gz

%changelog
* Thu Oct 13 2022 Sébastien Le Roux <sebastien.leroux@ipcms.unistra.fr> - 1.1.7-8
- Bug correction:
  callback.c: save workspace
  atom_action.c: on remove, trigger re-calculate bonding

* Tue Oct 11 2022 Sébastien Le Roux <sebastien.leroux@ipcms.unistra.fr> - 1.1.6-7
- Bug correction: 
  w_library.c: lib_preview_plot = NULL;
- Improvements:
  main.c: -h
  glview.c: selection delay on mouse pressed/released

* Fri Sep 23 2022 Sébastien Le Roux <sebastien.leroux@ipcms.unistra.fr> - 1.1.5-6
- Bug correction:
  w_search.c: selection not to crash if atom_win is closed

* Thu Sep 22 2022 Sébastien Le Roux <sebastien.leroux@ipcms.unistra.fr> - 1.1.4-5
- Bug correction: 
  read_coord.c: Windows to handle properly EOL symbols
  m_curve.c: Windows to not crash when destroying label widget
  glview.c: correct GWARNING messages on widget scale

* Thu Sep 15 2022 Sébastien Le Roux <sebastien.leroux@ipcms.unistra.fr> - 1.1.3-4
- Bug correction: 
  read_opengl.c: correct 'read_atom_b'
  initring.c: coorect 'send_rings_opengl_'

* Wed Sep 14 2022 Sébastien Le Roux <sebastien.leroux@ipcms.unistra.fr> - 1.1.2-3
- Bug correction: 
  atom_action.c: recompute bonding on passivate
  bdcall.c: do not trigger menu init on passivate

* Tue Sep 13 2022 Sébastien Le Roux <sebastien.leroux@ipcms.unistra.fr> - 1.1.1-2
- Bug correction: 
  double click on workspace

* Mon Aug 29 2022 Sébastien Le Roux <sebastien.leroux@ipcms.unistra.fr> - 1.1.0-1
- Initial release of the Atomes program v1.1.0
