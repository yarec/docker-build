
DIRS := $(shell find . ! -name "." -maxdepth 1 -type d |sed s@./@@g)

# Everything after this is generic

.PHONY: all
all: $(DIRS)
	#echo $(DIRS)

define PROGRAM_template
.PHONY: $1
$1:
	docker build -t yarec/$(strip $1) ./$(strip $1)
endef

$(foreach prog,$(DIRS), $(eval $(call PROGRAM_template, $(strip $(prog)))))


sync:
	cp -r ../src/service/ai-\>/keras .
