{
  inputs.nixpkgs.url = "github:nixos/nixpkgs/nixpkgs-unstable";
  inputs.flake-parts.url = "github:hercules-ci/flake-parts";
  inputs.systems.url = "systems";

  outputs = { self, flake-parts, ... }@inputs: flake-parts.lib.mkFlake { inherit inputs; } {
    systems = import inputs.systems;
    perSystem = { pkgs, ... }: {
      # Cheating: use flask directly instead of properly compiling
      packages.default = pkgs.writeShellApplication {
        name = "triangle-calc";
	runtimeInputs = [ pkgs.python3.pkgs.flask ];
	text = ''
	  d="$(mktemp -d)"
	  cp -r ${./.}/. "$d"
	  cd "$d"
	  exec flask run "$@"
	'';
      };
    };
  };
}