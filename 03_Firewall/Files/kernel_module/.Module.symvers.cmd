cmd_/home/tim/Dokumente/Uni/Ethical_Hacking/Challenge_3/Files/kernel_module/Module.symvers := sed 's/\.ko$$/\.o/' /home/tim/Dokumente/Uni/Ethical_Hacking/Challenge_3/Files/kernel_module/modules.order | scripts/mod/modpost -m -a  -o /home/tim/Dokumente/Uni/Ethical_Hacking/Challenge_3/Files/kernel_module/Module.symvers -e -i Module.symvers   -T -