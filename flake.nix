{
  description = "A Nix flake for cptool-py";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-24.11";
  };

  outputs = { self, nixpkgs, ... }: {
    packages.x86_64-linux = let
      pkgs = nixpkgs.legacyPackages.x86_64-linux;
    in {
      cptool-py = pkgs.python3Packages.buildPythonPackage {
        pname = "cptool-py";
        version = "1.1.3";
        src = ./.;
        nativeBuildInputs = [ pkgs.python3Packages.setuptools ];

        meta = with pkgs.lib; {
          description = "CLI for creating competitive programming problem files";
          license = licenses.mit;
          platforms = platforms.all;
        };
      };
    };

    defaultPackage.x86_64-linux = self.packages.x86_64-linux.cptool-py;
  };
}

